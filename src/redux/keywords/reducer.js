import actions from "./actions";

const initState = {
  keywords: JSON.parse(localStorage.getItem("keywords")) || [],
};

const reducer = (state = initState, { type, payload }) => {
  switch (type) {
    case actions.SET_KEYWORDS:
          if(!payload) return state;
          localStorage.setItem("keywords",JSON.stringify(payload));
          return Object.assign({}, state, { 
              ...state,
              keywords: payload 
            });
    default: return state;
  }
};

export default reducer;
