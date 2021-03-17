/* eslint-disable no-unused-vars */
import { BrowserRouter, Route, Switch, Link } from 'react-router-dom';

import { withAuthenticator } from 'aws-amplify-react';
import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js';
Amplify.configure(aws_exports);

function Home() {
    return (
        <div className="Home">
            <h1>Gen Five</h1>
            <p>Welcome to our battle simulator.</p>
            <h2>Your Characters</h2>
            <a href="/Creation">
                <button> Create a New Character </button></a>
            <br /><br />
            <h2>Your Parties</h2>
            <a href="/">
                <button> Create a Party </button></a>
            <br /><br /><br />
            <a href="/Battle">
                <button> Start Battle </button></a>
        </div >

    );
}
//export default Home;
export default withAuthenticator(Home, { includeGreetings: false });
