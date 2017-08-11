import { NOTIFICATIONS } from './constants';

export function notifications(
  state = { open: false, notifications: '' },
  action
) {
  switch (action.type) {
    case NOTIFICATIONS:
      return action.payload;
    default:
      return state;
  }
}
