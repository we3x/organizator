import { combineReducers } from 'redux';
import login from './pages/login/reducers';
import settings from './templates/default/reducers';
import theme from './containers/reducers';
import { notifications } from './containers/app/reducers';

const reducers = {
  login,
  notifications,
  theme,
};

settings.forEach(reducer => { reducers[reducer.name] = reducer; });

const rootReducer = combineReducers(reducers);

export default rootReducer;
