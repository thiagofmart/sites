const SERVER = "http://127.0.0.1:8000";


function get_posts () {
  const request = new XMLHttpRequest();
  request.open("GET", SERVER+"/post/get_all/", true);
  request.send();
  return request
}

function readLocalStorage() {
  if (!window.localStorage) {
    return
  }
}

function renderPostsBoard(posts) {
  var postsBoard = document.querySelector('.row');
  postsBoard.innerHTML = '';

  for (var i=0; i<posts.length; i++) {
    postsBoard.innerHTML+=`
    <div class="column">
      <article class="card">
        <a href="./assets/posts/page.html">
          <div class="card-image">
            <img src="./assets/images/Temp.png" alt="No Image FOUND">
          </div>
          <div class="card-text">
            <h3>Title</h3>
            <p>Long descriptaion of the post that you want to show in the home page Long descriptaion of the post that you want to show in the home page Long descriptaion of the post that you want to show in the home page...</p>
          </div>
        </a>
      </article>
    </div> `;
  }
}

function start() {
  var request = get_posts();
  request.onload = () => {
    if (request.status === 200) {
      console.log(JSON.parse(request.response))
      renderPostsBoard(JSON.parse(request.response));
    } else {
      console.log("Page not found")
    }
  }

}

start()
