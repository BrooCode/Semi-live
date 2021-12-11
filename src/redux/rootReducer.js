import { combineReducers } from "redux";
import keyword from './keywords/reducer'
const rootReducers = combineReducers({
  keyword: keyword,
});

export default rootReducers;
