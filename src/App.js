import Body from "./components/body";
import Head from "./components/head";
import Keywords from "./components/keywords";
import Leftbar from "./components/leftbar";
import "./styles.css";
import store from "./redux/store";
import { Provider } from "react-redux";
export default function App() {
  return (
    <Provider store={store}>
    <div className="App position-relative">
      <Head />
      <div className="d-flex justify-content-between align-items-center w-100 h-100 flex-wrap">
        <Leftbar />
        <Body />
        <Keywords />
      </div>
    </div>
    </Provider>
  );
}
