function Task1Done(boy)
{

var bulletstyle=document.getElementById(boy).style.textDecoration;
if(bulletstyle=='line-through')
	document.getElementById(boy).style.textDecoration='none';
  else
  document.getElementById(boy).style.textDecoration='line-through';

}
function clearAll()
{
	names = document.getElementsByClassName("task");
	for (i=0; i<names.length; i++)
	{
		names[i].style.textDecoration="none";
	}
}

function addListItem(text)
	{
  list = document.querySelector('ul');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}

function AddItem(){
	var i= prompt ("Enter the item to add list");
	addListItem(i);
}
