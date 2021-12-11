import React, { useEffect } from 'react'
import { useSelector } from 'react-redux';
import Keys from '../demoData'
const Keywords = () => {
    const keywords = useSelector((state) => state.keyword.keywords);
    useEffect(() => {
      console.log("keywords -->", keywords);
    },[keywords])
    return (
      <div className="d-flex flex-column align-items-center justify-content-center mt-md-2" style={{gap:'20px'}}>
      <div className="keywords mx-5 d-flex flex-column" style={{height:'min-content'}}>
       <div className={"keys d-flex justify-content-around align-items-center"/*+(i>0 ? "" : " first-key")*/}>
                <label className="container d-flex justify-content-around align-items-center">
                <span className="key-bold">Keyword</span>
              </label></div>
        </div>
        <div className="keywords mx-5 d-flex flex-column">
           <>
            {keywords.length > 0 ? keywords.map((a,i) =>{
                return (<div id={i} className={"keys d-flex justify-content-around align-items-center"}>
                <label className="container d-flex justify-content-around align-items-center">
             <input type="checkbox" />
                <span className="checkmark"></span>
                <span >{a[0]}</span>
              </label></div>)
            }) : (
              <div className="keys d-flex justify-content-around align-items-center">
                <label className="container d-flex justify-content-around align-items-center w-100">
                Search keywords
              </label></div>
            )}
            </>
        </div>
        </div>
    )
}

export default Keywords
