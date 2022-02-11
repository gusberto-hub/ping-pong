import { slide as Menu } from 'react-burger-menu';
import { useNavigate } from 'react-router-dom';
import './styles.scss';
// import MenuClosed from '../../assets/icons/menu.svg';
// import MenuOpen from '../../assets/icons/menu_open.svg';

export const MenuBar = () => {
  // for react router to change page
  let navigate = useNavigate();
  const HomeLink = () => {
    navigate('/');
  };

  const handleLogout = (event) => {
    // event.preventDefault();
    localStorage.clear();
    HomeLink();
  };

  return (
    <>
      <Menu isOpen={false} right width={'100vw'}>
        <a className='/' href='/'>
          Home
        </a>
        <a className='menu-item' href='/register'>
          Register
        </a>
        <a className='menu-item' href='/login'>
          Login
        </a>
        <span onClick={handleLogout}>
          <a className='menu-item' href='/'>
            Log out
          </a>
        </span>
        <a className='menu-item' href='/listing'>
          Listing
        </a>
        <a className='menu-item' href='/job'>
          Job
        </a>
        <a className='menu-item' href='/job/new'>
          New Job
        </a>
        <a className='menu-item' href='/job/private'>
          Private Job
        </a>
        <a className='menu-item' href='/helper'>
          Helper-Profile
        </a>
        <a className='menu-item' href='/member'>
          Member-Profile
        </a>
      </Menu>
    </>
  );
};
