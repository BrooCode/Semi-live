import axios from 'axios';
import actions from './actions'

const getKeywords = (payload) => {
    return (dispatch) => {
      dispatch({
        type: actions.SET_KEYWORDS,
        payload: payload,
      });
    };
  };
  
export default getKeywords;