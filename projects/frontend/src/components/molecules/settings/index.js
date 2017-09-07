import React, { Component } from 'react';
import LogoutIcon from 'material-ui/svg-icons/action/input';
import MenuItem from 'material-ui/MenuItem';
/* import { postLogoutURL } from '../../../constants';*/
import { withRouter } from 'react-router';

const styles = {
  settings: {
    item: {
      cursor: 'pointer',
    },
  },
};

@withRouter
class Settings extends Component {
  handleLogout() {
    // eslint-disable-next-line no-undef
    window.localStorage.removeItem('OrganizatorAuthToken');
    console.log(this);
  }

  render() {
    return (

      <MenuItem
        primaryText="Logout"
        leftIcon={<LogoutIcon />}
        onTouchTap={this.handleLogout}
        style={styles.settings.item}
      />
    );
  }
}

export default Settings;
