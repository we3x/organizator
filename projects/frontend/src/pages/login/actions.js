import { createAction } from 'redux-actions';
import { fetch } from '../../utils';
import LOGIN from './constants';

const reset = createAction(LOGIN, () => ({
  status: 'initial',
}));

const begin = createAction(LOGIN, () => ({
  status: 'pending',
}));

const success = createAction(LOGIN, json => {
  // eslint-disable-next-line no-undef
  window.localStorage.OrganizatorAuthToken = json.token;
  return {
    token: json.token,
    status: 'success',
  };
});

const fail = createAction(LOGIN, error => ({
  error: error.message,
  status: 'error',
}));

const login = (username, password) =>
  (dispatch) => {
    dispatch(begin());
    const apiUrl = 'http://localhost:8000';
    fetch({
      url: `${apiUrl}/auth/`,
      body: {
        username,
        password,
      },
      contentType: 'application/json',
      method: 'POST',
    })
      .then(token => {
        dispatch(success(token));
        return token;
      })
      .catch(error => {
        dispatch(fail(error));
      });
  };

const actions = {
  reset,
  begin,
  success,
  fail,
  login,
};

export default actions;
