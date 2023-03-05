import { Route, Routes } from 'react-router-dom';
import { Link } from 'react-router-dom';
import Home from './pages/Home';
import Rankings from './pages/Rankings';
import About from './pages/About';
import Data from './pages/Data';

import Container from 'react-bootstrap/Container';
import Nav from 'react-bootstrap/Nav';
import Navbar from 'react-bootstrap/Navbar';
import 'bootstrap/dist/css/bootstrap.min.css';
import './styles/navbar.css'

function App() {
  return (
    <>
      <Navbar bg="light" variant="light" style={{ height: '150px' }}>
        <Container>
        <Link to="/" className="nav-link"><img src={require('./assets/logo.gif')} alt="logo" id='logo'/></Link>
        <Nav className="me-auto">
          <Link to="Rankings" className="nav-link">Rankings</Link>
          <Link to="Data" className="nav-link">Data</Link>
          <Link to="About" className="nav-link">About</Link>
        </Nav>
        <a href='https://github.com/raunak8016/BadmintonBets' target="_blank" rel="noreferrer"><img src={require('./assets/git.png')} alt="git" id='git'/></a>
        <a href='https://www.linkedin.com/in/raunak-sandhu/' target="_blank" rel="noreferrer"><img src={require('./assets/linkedin.png')} alt="linkedin" id='git'/></a>
        </Container>
      </Navbar>

      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="Rankings" element={<Rankings />} />
        <Route path="Data" element={<Data />} />
        <Route path="About" element={<About />} />
        <Route path="*" element={<h1>404 - Not Found</h1>} />
      </Routes>
    </>
  );
}

export default App;
