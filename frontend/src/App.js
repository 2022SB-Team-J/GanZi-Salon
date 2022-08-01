import React from "react";
import { BrowserRouter as Router ,Route, Switch } from "react-router-dom";
import routespage from "./routespage";
import './index.css';
import {useSelector} from "react-redux";
import 'bootstrap/dist/css/bootstrap.min.css';
const App = () => {
    const token = useSelector((state) => state.Auth.token);
    console.log(token);


return (
    <div >
    
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
    </Router>
    
    </div>
);
}

export default App;
