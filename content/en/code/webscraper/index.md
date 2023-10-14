---
title: "Webscraper & HTML Text Comparison Tool"
description: ""
lead: ""
date: 2023-10-14T22:31:50-04:00
lastmod: 2023-10-14T22:31:50-04:00
draft: false
images: []
menu:
  docs:
    parent: "code-overview"
weight: 51
toc: true
---

One struggle I've had in decentralized documentation environments is knowing when someone else updates documentation that is maintained outside my purview. 

In one instance at work, several separate GitHub Pages sites were being maintained outside my purview, but I needed to know when updates were made on these sites so I could reconcile them with my documentation. Unfortunately, the other sites' maintainers wanted to keep their documentation efforts independent of mine, leaving me with a need to know when those other sites were updated. I also couldn't rely on the site maintainers to let me know when they made updates; people, it turns out, are forgetful.

The only solution to this problem was automation: a solution that would automatically check for site updates on a defined cadence and let me know what, if any changes, were present.

Below is my effort. I wrote this in Python over the course of a day or so. It's best suited for Mac and Linux machines, but it can be updated with minimal effort for Windows systems. Using `cron`, I set this to execute automatically every day at 9:00 am.

If you want to use this tool, simply update the URLs and labels in the Python dictionary. I've added functions whereby you can indicate if you want to check for other websites at run time. This function is currently turned off; to turn them on, reverse the `default` arguments in `__main__`.


```py
import os
from pathlib import Path
from bs4 import BeautifulSoup
import urllib3
import certifi
import difflib
from datetime import datetime
import webbrowser
import sys
import platform

python webScraper.py
# Constants

# Update before running code

HTML_BENCHMARKS_PATH = Path('/Users/benjaminmoran/Desktop/html-benchmarks/')
URL_DICT = {
    "cornell": "https://it.cornell.edu/web-hosting-static/how-test-your-static-sites",
    "wikipedia": "https://en.wikipedia.org",
    "portfolio_git": "https://benbarksdale.netlify.app/docs/guides/introduction-to-git-for-technical-writers/",
    "github_sphinx_test":"https://github.com/redsoxfan0219/sphinx-github-action"
}

# Other global variables

http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
date = datetime.now().strftime("%Y-%m-%d")  
def get_operating_system():
    if sys.platform.startswith("win"):
        operating_system = "windows"
    if sys.platform == "darwin":
        operating_system = "mac"
    else:
        operating_system = "linux"
    
    return operating_system
operating_system = get_operating_system()

site_list = []

## Define Site class

class Site:
    """
    Creates a site object to house name, url, and methods to get 
    html benchmark and current site html
    """

    def __init__(self, name: str, url: str):

        self.name = name
        self.url = url
        self.file_path = self.set_file_path()
        self.html_benchmark = self.get_html_benchmark()
        self.present_site_html = self.get_present_site_html()

    def get_url(self):
        """
        Getter for site's url attribute.
        """
        return self.url

    def set_url(self, url):
        """
        Setter for site's url attribute.
        """
        self.url = url
    
    def get_name(self):
        """
        Getter for site's name attribute.
        """
        return self.name

    def set_name(self, name: str):
        """
        Setter for site's name attribute.
        """
        self.name = name

    def set_file_path(self):
        """
        Setter for site's file_path attribute.
        """
        file_name = HTML_BENCHMARKS_PATH / f'{self.name}.html'
        return file_name

    def get_file_path(self):
        """
        Getter for site's file_path attribute.
        """
        return self.file_path

    def get_present_site_html(self):
        """
        GETs site's HTML from web.
        Returns string of HTML.
        """

        response = http.request('GET', self.url)
        if response.status == 200:
            soup = BeautifulSoup(response.data, 'html.parser')
            return soup.prettify()
        else:
            print(f"Failed to retrieve HTML for {self.name}. Status code: {response.status}")
            return None

    def get_html_benchmark(self):
        """
        Retrieves contents of HTML benchmark file and assigns to 
        html_benchmark attribute.
        """
        try:
            benchmark_file_path = HTML_BENCHMARKS_PATH / f'{self.name}.html'
            if os.path.exists(benchmark_file_path):
                with open(benchmark_file_path, 'r') as f:
                    file_contents = f.read()
                return file_contents
            else:
                self.create_new_html_benchmark()
                ColoredOutput.print_blue(f"Creating a new HTML benchmark for {self.name}")
                print("")
                return self.html_benchmark
        
        except Exception:
            return None

    def create_new_html_benchmark(self):
        """
        Creates a new HTML benchmark file and assigns file's contents to 
        html_benchmark attribute.
        """
        benchmark_file_path = HTML_BENCHMARKS_PATH / f'{self.name}.html'
        if not os.path.exists(benchmark_file_path):
            file_contents = self.get_present_site_html()
            with open(benchmark_file_path, 'w+') as f:
                f.write(file_contents)
            self.html_benchmark = file_contents


    def replace_existing_benchmark(self):
        """
        Replaces existing benchmark file with one based on
        site's current HTML.

        Intended for execution at end of program.
        """
        benchmark_file_path = HTML_BENCHMARKS_PATH / f'{self.name}.html'
        if os.path.exists(benchmark_file_path):
            with open(benchmark_file_path, 'w') as f:
                file_contents = self.present_site_html
                f.write(file_contents)
            self.html_benchmark = file_contents

    def produce_differences_file_benchmark_and_present_html(self):

        """
        Creates an output HTML file comparing benchmark and current HTML.
        Sets comparison_file attribute equal to path of comparison file.
        """

        benchmark_split = self.html_benchmark.splitlines()
        present_html_split = self.present_site_html.splitlines()

        differ = difflib.HtmlDiff(wrapcolumn=70)
        table_of_diffs = differ.make_file(benchmark_split, present_html_split)
        target_file = HTML_BENCHMARKS_PATH.joinpath(f"{self.name}_benchmark_present-comparison-{date}.html")        
        with open(target_file, 'w+') as f:
            f.write(table_of_diffs)
        self.comparison_file = target_file
        self.comparison_created_already_today = True

    def open_comparison_file_with_browser(self):

        """
        Opens comparison file if one exists.
        """

        if hasattr(self, 'comparison_file'):

            try:
                if operating_system in ["mac", "linux"]:
                    webbrowser.open_new_tab(f'file://{self.comparison_file}')
                else:
                    webbrowser.open_new_tab(self.comparison_file)
                
            except Exception as e:
                print(f"An error occurred: {e}")

    def check_for_sameday_comparison(self):

        """
        Sets attribute if comparison file has been generated already today.
        """

        for file in os.listdir(HTML_BENCHMARKS_PATH):
            if f"{self.name}_benchmark_present-comparison-{date}.html" == file:
                self.comparison_created_already_today = True


class ColoredOutput:
    """
    A class for changing text color in standard output.
    """

    # ANSI escape codes for text colors
    RED = "\033[91m"
    BLUE = "\033[94m"
    RESET = "\033[0m"  # Reset color to default

    @staticmethod
    def print_red(text):
        """
        Print text in red color.
        """
        print(ColoredOutput.RED + text + ColoredOutput.RESET)

    @staticmethod
    def print_blue(text):
        """
        Print text in blue color.
        """
        print(ColoredOutput.BLUE + text + ColoredOutput.RESET)

# Alternatively, you can use platform.system()
os_name = platform.system()


def _use_different_sites(use_defaults=False):
    """
    Provides user chance to build their own URL_DICT
    Can silence in future runs by setting use_defaults=True
    """
    global URL_DICT

    if URL_DICT:
        ColoredOutput().print_red("\nA dictionary of sites has already been defined in webScraper.py.\n")
        user_input = input("Use the present dictionary?  ")
        if user_input.lower() in ["no", "n"]:
            add_another_entry = ""
            while add_another_entry.lower() not in ["no", "n"]:
                user_defined_urls_dict = {}
                site_shortname = input("Enter a shortname for the site (not URL):  ")
                site_url = input("Enter URL:  ")
                user_defined_urls_dict[site_shortname] = site_url
                add_another_entry = input("Add another site to list?  ")

            URL_DICT = user_defined_urls_dict

def _check_user_benchmark_preference(default=False):

    """
    Checks if user wants to change HTML benchmarks path.
    Can be silenced for future runs by setting default=True.
    """

    global HTML_BENCHMARKS_PATH

    if default:
        return

    print(f"Default path for html benchmarks is: {HTML_BENCHMARKS_PATH}\n")

    choice = input("Use a different path for HTML benchmarks folder? ")

    while True:
        if choice.lower() in ("yes", "y"):
            user_entry = input("Enter an absolute path: ")
            user_provided_dir = Path(user_entry)

            if user_provided_dir.is_absolute():
                new_path = user_provided_dir / "html-benchmarks"

                if not new_path.exists():
                    try:
                        new_path.mkdir(parents=True)
                        if new_path.exists():
                            print(f"Created directory at {new_path}")
                            HTML_BENCHMARKS_PATH = new_path
                            break
                    except OSError as e:
                        print(f"Error creating directory: {e}")
                else:
                    HTML_BENCHMARKS_PATH = new_path
                    print(f"{new_path} set as the path for benchmarks")
                    break
            else:
                print("Invalid path provided.")
        else:
            _create_benchmarks_directory()
            break

def _create_benchmarks_directory():

    """
    Creates benchmarks directory if it doesn't already exist.
    """

    if not HTML_BENCHMARKS_PATH.exists():
        os.mkdir(HTML_BENCHMARKS_PATH)

def _create_site_list():

    """
    Creates list of Site objects based on the key-value
    pairs listed in the URL_DICT
    """

    try:
        for name, url in URL_DICT.items():
            site = Site(name, url)
            site_list.append(site)

    except Exception as e:
        print(f'Error: {e}')

def _update_benchmarks():

    print("Updating benchmarks...")

    for site in site_list:
        site.replace_existing_benchmark()

    print("Benchmarks updated.")  

def _compare_benchmark_and_present_html():

    """
    If there is a difference between the benchmark and the present HTML,
    offers to produce a comparison of the two.
    
    Checks if a comparison file has already been produced. 
    
    User can recreate daily comparison file. 

    If no benchmark exists, creates a new benchmark.
    """

    for site in site_list:
        if site.html_benchmark is not None:
            if site.html_benchmark != site.present_site_html:
                ColoredOutput.print_red(f"\nWARNING: Difference between {site.get_name()}'s benchmark and present site")
                user_option = input("\nCreate an HTML table of the deltas? ")
                if user_option.lower() == "yes" or user_option.lower() == "y":
                    site.check_for_sameday_comparison()
                    if hasattr(site, "comparison_created_already_today"):
                        rerun_comparison = input(f"\nA comparison file has already been created today for {site.name}. Replace comparison file? ")
                        if rerun_comparison.lower() == "yes" or rerun_comparison.lower() == "y":
                            site.produce_differences_file_benchmark_and_present_html()
                    else:
                        site.produce_differences_file_benchmark_and_present_html()
                
            else:
                print("")
                ColoredOutput.print_blue(f"No difference between {site.get_name()}'s benchmark and present site detected")
                print("")
        else:
            print("")
            ColoredOutput.print_blue(f"\nNo existing benchmark for {site.get_name()}.")
            ColoredOutput.print_blue("Creating new benchmark file for future comparisons.\n")
            site.create_new_html_benchmark()

    if hasattr(site, 'comparison_created_already_today'):
        wants_to_open_comparison_files = input("Want to open the file(s) outlining the deltas? ")
        if wants_to_open_comparison_files.lower() in ["yes","y"]:
            for site in site_list:
                site.open_comparison_file_with_browser()

if __name__ == "__main__":

    ColoredOutput()
    _use_different_sites(default=True)
    _check_user_benchmark_preference(default=True)
    _create_site_list()
    _compare_benchmark_and_present_html()
    _update_benchmarks()
```

