import MeetingRoomIcon from '@material-ui/icons/MeetingRoom';
import DoubleArrowIcon from '@material-ui/icons/DoubleArrow';
import { useEffect, useState } from 'react';
import {useDispatch} from 'react-redux';
import getKeywords from '../redux/keywords/actionCreators';
import axios from 'axios';

const Body = () => {
  const [selectedFile, setSelectedFile] = useState("");
  const dispatch = useDispatch();
  const [loading, setloading] = useState(false);
  const changeHandler = async (event) => {
    event.preventDefault();
    setloading(true);
     setSelectedFile(event.target.files[0])
  }
  const postIt = async () => {
    console.log("selectedFile",selectedFile);
    var data = new FormData();
    data.append('file', selectedFile);
    const res = await axios.post('http://localhost:8000/awesome',data);
    dispatch(getKeywords(res.data.result));
    setloading(false);
  }
  useEffect(() => {
    console.log("selectedFile",selectedFile);
    if(selectedFile !== ""){
      postIt();
    }
  },[selectedFile]);

  useEffect(() => {

  },[])
  return <>{loading ? (<div>Loading...</div>) : <div className="d-flex flex-column justify-content-center align-items-center col-8">
    <div className="dragit">
      <label className="w-100 h-100 d-flex justify-content-center align-items-center" htmlFor="uploadvideo">Drag and Drop</label>
      <input id="uploadvideo" type="file" accept="video/mp4" onChange={changeHandler} webkitdirectory/>
    </div>
    <div className="d-flex justify-content-center align-items-center">
    <div className="txt-msg mt-4">
      <p>Type all questions and answers or upload the text file</p>
    </div>
   <div className="d-flex txt-icons"><DoubleArrowIcon fontSize="large"/><MeetingRoomIcon fontSize="large" /></div> 
   </div>
  </div>}</>;
};

export default Body;
