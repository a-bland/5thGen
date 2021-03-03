import '../App.css';
import 'antd/dist/antd.css';
import { Typography } from 'antd';

import Amplify, { API, graphqlOperation } from 'aws-amplify';
import aws_exports from '../aws-exports.js'; // specify the location of aws-exports.js file on your project
Amplify.configure(aws_exports);

const { Title } = Typography;

function Creation() {
    return (
        <div className="Creation">
            <Title>Create Your Character</Title>
            <p>Choose wisely!</p>
            <p>Character name: </p>
            <a href="/">
                <button> Save Character </button>
            </a>
        </div>

    );
}

export default Creation;