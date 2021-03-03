import './App.css';
import 'antd/dist/antd.css';
import { Typography } from 'antd';
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom';
import Battle from './components/Battle';
import Creation from './components/Creation';
import Home from './components/Home';

import Amplify, { API, graphqlOperation } from 'aws-amplify';
import { withAuthenticator } from 'aws-amplify-react';
import aws_exports from './aws-exports.js'; // specify the location of aws-exports.js file on your project
Amplify.configure(aws_exports);

const { Title } = Typography;

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Switch>
          <Route exact path="/" component={Home}></Route>
          <Route path="/Battle.html" component={Battle}></Route>
          <Route path="/Creation.html" component={Creation}></Route>
        </Switch>
      </BrowserRouter>
    </div >

  );
}
export default App;
