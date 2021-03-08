/* eslint-disable no-unused-vars */
import './App.css';
import 'antd/dist/antd.css';
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom';
import Battle from './components/Battle';
import Creation from './components/Creation';
import Home from './components/Home';

import Amplify, { API, graphqlOperation } from 'aws-amplify';
import { withAuthenticator } from 'aws-amplify-react';
import aws_exports from './aws-exports.js';
Amplify.configure(aws_exports);

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Route path="/Battle" component={Battle}></Route>
          <Route path="/Creation" component={Creation}></Route>
        </Switch>
      </BrowserRouter>
    </div >

  );
}
export default App;
