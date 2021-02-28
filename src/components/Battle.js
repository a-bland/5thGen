//import './App.css';
import 'antd/dist/antd.css';
import { Typography } from 'antd';

import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js'; // specify the location of aws-exports.js file on your project
Amplify.configure(aws_exports);

const { Title } = Typography;

function Battle() {
    return (
        <div className="Battle">
            <Title>Battle Simulator</Title>
            <p>Fight!</p>
            <a href="/">
                <button> End Battle </button>
            </a>
        </div>

    );
}

export default Battle;