import React from 'react';
import loader from '../assets/SVG/loader.svg';

const Loader = ({text}) => {
    return (
        <div className="d-flex flex-column justify-content-center align-items-center">
            <img src={loader} />
            <span>{text}</span>
        </div>
    )
}

export default Loader
