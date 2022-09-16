const SERVER = "http://127.0.0.1:8000";
const subject = ["Filosofia", "Matemática", "string", "IoT", "Física", "Economia"]

// verify if an obj is in array
Array.prototype.contains = Array.prototype.contains || function(obj)
{
  var i, l = this.length;
  for (i = 0; i < l; i++)
  {
    if (this[i] == obj) return true;
  }
  return false;
};


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
  var postsBoard = document.querySelector('.main');

  postsBoard.innerHTML = '';
  for (var i0=0; i0<subject.length; i0++){
    var row = "";

    var posts_qtd = posts.length;
    for (var i1=0; i1<posts.length; i1++) {

      if (posts[i1].subject.contains(subject[i0])) {
        row+=`
        <div class="column">
          <article class="card">
            <a href="./assets/posts/page.html">
              <div class="card-image">
                <img src="./assets/images/Temp.png" alt="No Image FOUND">
              </div>
              <div class="card-text">
                <h3>${posts[i1]['title']}</h3>
                <p>${posts[i1]['description']}</p>
              </div>
            </a>
            </article>
        </div>`;
      }
    }
    postsBoard.innerHTML+=`
    <h1 class="section-header blog">${subject[i0]}</h1>
    <div class="row">
      ${row}
    </div><br><hr>
    `
  }
}
//<p>Long descriptaion of the post that you want to show in the home page Long descriptaion of the post that you want to show in the home page Long descriptaion of the post that you want to show in the home page...</p>

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
