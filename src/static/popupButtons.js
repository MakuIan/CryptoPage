function openPopup(id) {
  var popup = document.getElementById(id);
  if (!popup) return;
  popup.classList.add("open-popup");
}
function closePopup(id) {
  var popup = document.getElementById(id);
  if (!popup) return;
  popup.classList.remove("open-popup");
}
function add(id) {
  var popup = document.getElementById(id);
  if (!popup) return;
  popup.style.visibility = "visible";
}
function search(id) {
  var popup = document.getElementById(id);
  if (!popup) return;
  popup.style.visibility = "visible";
}
