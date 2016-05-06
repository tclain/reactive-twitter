import React from 'react';
import { Router,IndexRoute, Route, Link, hashHistory } from 'react-router' ;
import VoidLayout from './ui/layouts/VoidLayout.jsx';


export default (
  <Router history={hashHistory}>
    <Route path="/" component={VoidLayout}>
    </Route>
  </Router>
);
