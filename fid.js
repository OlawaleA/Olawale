function Task1Done(boy)
{

var bulletstyle=document.getElementById(boy).style.textDecoration;
if(bulletstyle=='line-through')
	document.getElementById(boy).style.textDecoration='none';
  else
  document.getElementById(boy).style.textDecoration='line-through';

}
