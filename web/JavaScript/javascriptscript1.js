function agranda(){
element=document.getElementById("verde");
styleel=document.defaultView.getComputedStyle(element,null);
if (parseInt(parseInt(styleel.height))<300){
    element.style.height=(parseInt(styleel.height)+5)+'px';
}
else{
    console.log(parseInt(styleel.height));
    document.getElementById("verde").innerHTML = '<p>TAS PASAU!</p>';
    
}
    

}