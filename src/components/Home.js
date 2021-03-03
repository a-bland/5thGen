import 'antd/dist/antd.css';
import { Typography } from 'antd';
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom';

import { withAuthenticator } from 'aws-amplify-react';
import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js';
Amplify.configure(aws_exports);

const { Title } = Typography;

function Home() {
    return (
        <div className="Home">
            <Title>Gen Five</Title>
            <p>Welcome to our battle simulator.</p>
            <a href="/Creation">
                <button> Create a Character </button></a>
            <br /><br />
            <a href="/Battle">
                <button> Start Battle </button></a>
        </div >

    );
}
//export default Home;
export default withAuthenticator(Home, { includeGreetings: false });
