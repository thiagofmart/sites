const SERVER = "http://127.0.0.1:8000";

function _getPostIdFromUrl() {
  var arryUrlVariables = window.location.href.split('#')
  for (var i=0; i<arryUrlVariables.length; i++) {
    if (arryUrlVariables[i].includes("id")) {
      return arryUrlVariables[i].split("=")[1]
    }
  }
  return null
}

function _getPostByID(id) {
  const request = new XMLHttpRequest();
  request.open("GET", SERVER+`/post/by_id/?id=${id}`, true);
  request.send();
  return request
}
