import './App.css';
import 'antd/dist/antd.css';
import { Typography } from 'antd';

import Amplify, { API, graphqlOperation } from 'aws-amplify';
import { withAuthenticator } from 'aws-amplify-react';
import aws_exports from './aws-exports.js'; // specify the location of aws-exports.js file on your project
Amplify.configure(aws_exports);

const { Title } = Typography;

function App() {
  return (
    <div>
      <Title>Gen Five</Title>
      <p>Welcome to our battle simulator.</p>
    </div>

  );
}
//export default App;
export default withAuthenticator(App, { includeGreetings: false });
