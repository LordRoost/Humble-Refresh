var leftPrice;
var rightPrice;


var iframe = document.getElementById("lFrame");
var iframeDocument = iframe.contentDocument || iframe.contentWindow.document;
window.alert("hi");
var iframeContent;


if (iframeDocument){
	iframeContent = iframeDocument.getElementByClassName("prepend section-heading price bta");
	window.alert(iframeContent.value);
}


/*
function getFrameContents()
{
   var iFrame =  document.getElementById('lFrame');
   var iFrameBody;
   if ( iFrame.contentDocument ) 
   { // FF
     iFrameBody = iFrame.contentDocument.getElementsByTagName('body')[0];
   }
   else if ( iFrame.contentWindow ) 
   { // IE
     iFrameBody = iFrame.contentWindow.document.getElementsByTagName('body')[0];
   }
    alert(iFrameBody.innerHTML);
 }
 */