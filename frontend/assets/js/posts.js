const SERVER = "http://127.0.0.1:8000";

function _getPostIdFromUrl() {
  var arryUrlVariables = window.location.href.split('#')
  for (var i=0; i<arryUrlVariables.length; i++) {
    if (arryUrlVariables[i].includes("id")) {
      var postTopicID = arryUrlVariables[i].split("=")[1].split('.');
      return postTopicID
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

function render(post, topic) {
  document.querySelector('.title').innerHTML = post['title']
  document.querySelector('.description').innerHTML = topic['title']
  var article_field = document.querySelector('.article');
  article_field.innerHTML = "";

  article_field.innerHTML = `
    <h2>${topic['title']}</h2>
    <p>${topic['content']}</p>
    `;
}

function start() {
  var postTopicID = _getPostIdFromUrl();
  var post_request = _getPostByID(postTopicID[0]);
  var topic_request = _getTopicByID(postTopicID[1]);
  post_request.onload = () => {
    topic_request.onload = () => {
        if (post_request.status === 200 & topic_request.status === 200) {
        console.log(JSON.parse(post_request.response));
        console.log(JSON.parse(topic_request.response));
        var post = JSON.parse(post_request.response);
        var topic = JSON.parse(topic_request.response);
        render(post, topic);
        }
    } else {
      console.log("Page not found");
    }
  }
}

start();
