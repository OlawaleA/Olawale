function addListItem(text){
  list = document.querySelector('ul');
  item = document.createElement('li');
  item.innerText = text;
  list.appendChild(item);
}
addListItem("mango")
addListItem("apple")
addListItem("strawberries")
addListItem("grapes")
// Now use the function to add elements to the list!
