import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import PredictionPage from './pages/PredictionPage';
import Header from './components/Header';
import Footer from './components/Footer';

const App: React.FC = () => {
    return (
        <Router>
            <div className="App">
                <Header />
                <Switch>
                    <Route path="/" exact component={PredictionPage} />
                </Switch>
                <Footer />
            </div>
        </Router>
    );
};

export default App;