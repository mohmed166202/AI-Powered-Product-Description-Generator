import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './pages/Home';
import Settings from './pages/Settings';
import Dashboard from './components/Dashboard';
import LanguageSelector from './components/LanguageSelector';

const App = () => {
  return (
    <Router>
      <div className="app-container">
        <LanguageSelector />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/settings" component={Settings} />
          <Route path="/dashboard" component={Dashboard} />
        </Switch>
      </div>
    </Router>
  );
};

export default App;