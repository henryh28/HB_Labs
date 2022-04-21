function App() {
  const [melons, setMelons] = React.useState({});
  const [shoppingCart, setShoppingCart] = React.useState({});


  React.useEffect(() => {
    const fetchData = async () => {
      const response = await fetch('/api/melons')
      const melonData = await response.json()
      setMelons(melonData);
    }

    fetchData();
  }, []);

  function addMelonToCart(melonCode) {
    setShoppingCart(currentShoppingCart => {
      const newShoppingCart = Object.assign({}, currentShoppingCart);

      newShoppingCart[melonCode] = melonCode in newShoppingCart ? newShoppingCart[melonCode] + 1 : 1;

      return newShoppingCart
    })
  }


    return (
    <ReactRouterDOM.BrowserRouter>
      <Navbar logo="/static/img/watermelon.png" brand="Ubermelon" />
      <div className="container-fluid">
        <ReactRouterDOM.Route exact path="/">
          <Homepage />
        </ReactRouterDOM.Route>
        <ReactRouterDOM.Route exact path="/shop">
          <AllMelonsPage melons={melons} addMelonToCart={addMelonToCart} />
        </ReactRouterDOM.Route>
        <ReactRouterDOM.Route exact path="/cart">
          <ShoppingCartPage cart={shoppingCart} melons={melons}/>
        </ReactRouterDOM.Route>
      </div>
    </ReactRouterDOM.BrowserRouter>
  );
}

ReactDOM.render(<App />, document.querySelector('#root'));
