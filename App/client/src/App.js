import { Route, Routes } from 'react-router-dom';
import { Link } from 'react-router-dom';
import Home from './pages/Home';
import Rankings from './pages/Rankings';
import About from './pages/About';

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';


function App() {
  return (
    <>
      <Navbar bg="light" variant="light">
        <Container>
        <Link to="/" className="nav-link"><img src={require('./assets/logo.png')} alt="logo" /></Link>
        <Nav className="me-auto">
          <Link to="/" className="nav-link">Home</Link>
          <Link to="Rankings" className="nav-link">Rankings</Link>
          <Link to="About" className="nav-link">About</Link>
          <a href='https://github.com/raunak8016/BadmintonBets'><img src={require('./assets/git.png')} alt="git" /></a>
        </Nav>
        </Container>
      </Navbar>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="Rankings" element={<Rankings />} />
        <Route path="About" element={<About />} />
        <Route path="*" element={<h1>404 - Not Found</h1>} />
      </Routes>
    </>
  );
}

export default App;
