import React, { useEffect, useState } from 'react'
import { useSelector } from 'react-redux';
import Keys from '../demoData'
const Keywords = () => {
    const keywords = useSelector((state) => state.keyword.keywords);
    const [selectedKey, setselectedKey] = useState([]);
    useEffect(() => {
      console.log("keywords -->", keywords);
    },[keywords])
    const selectThisKeyword = (i, keyword,e,type) =>{
      let checkarr = selectedKey.filter(a => a.id === i);
      if(type === "text"){
          let value = e.target.value;
          checkarr = selectedKey.filter(a => a.id !== i);
          checkarr.push({id:i,tag: keyword,answer: value});
          setselectedKey(checkarr);
      }else{
        if(checkarr.length > 0){
          checkarr = selectedKey.filter(a => a.id !== i);
          setselectedKey(checkarr);
        }else{
          setselectedKey(prevState => [...prevState, {id:i,tag: keyword,answer: i}]);
        }
      }
     
    }
    useEffect(() => {console.log("selectedKey",selectedKey)},[selectedKey])
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
                return (
                <div id={i} className={"keys d-flex justify-content-around align-items-center position-relative"}>
                <label className="container d-flex justify-content-around align-items-center">
                <input className="checkbox" type="checkbox" onChange={(e) => selectThisKeyword(i,a[0],e, "checkbox")}/>
                <span className="checkmark"></span>
                {selectedKey.filter(a => a.id === i).length === 0 && <div className="key">{a[0]}</div>}
                </label>
                {selectedKey.filter(a => a.id === i).length > 0 && <input className="typeKey" type="text" placeholder='Type answer..'  onChange={(e) => selectThisKeyword(i,a[0],e, "text")}/>}
                </div>
              )
            }) : (
              <div className="keys d-flex justify-content-around align-items-center">
                <label className="container d-flex justify-content-around align-items-center w-100">
                No Keywords
              </label></div>
            )}
            </>
        </div>
        </div>
    )
}

export default Keywords
