---
title: "Process Flow"
description: ""
date: 2022-06-23T01:10:48-04:00
lastmod: 2022-06-23T01:10:48-04:00
draft: false
images: []
---

Process flow maps are vital to technical documentation. Whether used to describe business processes or data product architecture, they help everyone get on the same page by visualizing the abstract.

There are several software programs out there that can be used to create process flow maps. I'm most familiar with [Microsoft Visio](https://www.microsoft.com/en-us/microsoft-365/visio/flowchart-software), a program in which I've developed custom templates and [custom stencils](https://support.microsoft.com/en-us/office/create-save-and-share-custom-stencils-a4c2235c-677d-4117-9673-1fef0a0ee22f). I am also familiar with [Miro](https://miro.com/online-whiteboard/) and [FigJam](https://www.figma.com/figjam/), for which I've build basic plugins using TypeScript via the [Figma Plugin API](https://www.figma.com/plugin-docs/intro/).

In my past work, I have used process flow maps primarily to visualize how AI/ML models are structured.  With the help of my process flow maps, confused business partners and those outside the dev project team can begin to understand how a data product is functioning.

Below is a generic example of the kind of diagram I complete regularly in Visio. As you can see, this diagram visualizes how data comes into a model, how it is transformed, how it is processed, and what happens to outputs after they are produced.

<div id="adobe-dc-view" style="height: 360px; width: 500px;"></div>
<script src="https://documentcloud.adobe.com/view-sdk/main.js"></script>
<script type="text/javascript">
	document.addEventListener("adobe_dc_view_sdk.ready", function(){ 
		var adobeDCView = new AdobeDC.View({clientId: "e35d36790e954c329c2f2e8355919a72", divId: "adobe-dc-view"});
		adobeDCView.previewFile({
			content:{location: {url: "https://github.com/redsoxfan0219/portfolio/blob/27ebcf1cb970d7e4999c819cef0400a738b73bac/content/en/graphics/processflow/Sample-ML-Visio-Diagram.pdf"}},
			metaData:{fileName: "Sample Process Flow.pdf"}
		}, {embedMode: "SIZED_CONTAINER"});
	});
</script>


