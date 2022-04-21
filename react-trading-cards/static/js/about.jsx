'use strict';

function About() {
  return (
          <React.Fragment>
            <div id="About the Author">
                <p>Name: Henry Hsu</p>
                <a href = "https://github.com/henryh28">My Github profile</a>
            </div>
          </React.Fragment>
  );
}

ReactDOM.render(<About />, document.querySelector('#about'));
