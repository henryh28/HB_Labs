'use strict';

function Homepage() {
  return (
          <React.Fragment>
            <div>Welcome user!</div>
            <div id="balloonicorn_logo">
              <img src="static/img/balloonicorn.jpg"></img>
            </div>
            <p><a href="/cards">Go to cards</a></p>
            <p><a href="/about">About the Author</a></p>
          </React.Fragment>
  );
}

ReactDOM.render(<Homepage />, document.querySelector('#app'));
