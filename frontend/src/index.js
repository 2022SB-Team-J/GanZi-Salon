import React from 'react';
import ReactDOM from 'react-dom';
import App from './App';
import {Provider} from "react-redux";
import store from "./redux/configStore";
import {PersistGate} from "redux-persist/integration/react";
import persistStore from "redux-persist/es/persistStore";

const persistor = persistStore(store)
const root = ReactDOM.createRoot(document.getElementById("root"));

root.render(
    <Provider store={store}>
    <PersistGate persistor={persistor}>

    <App />

</PersistGate>
  </Provider>
);
document.getElementById('root')


