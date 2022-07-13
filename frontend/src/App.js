import React from "react";
import { BrowserRouter as Router ,Route, Switch } from "react-router-dom";
import routespage from "./routespage";
import './index.css';


function App() {
return (
    <div className="App">
    <Router>
        <Switch>
        {routespage.map((route) => {
            return (
            <Route path={route.page} key={route.page} exact>
                <route.component />
            </Route>
            );
        })}
        </Switch>
    </Router>{" "}
    </div>
);
}

export default App;