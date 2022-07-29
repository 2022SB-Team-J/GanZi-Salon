import Upload from './pages/Upload';
import Title from './pages/Title';
import ChooseStyle from './pages/ChooseStyle';
import AppliedStyle from './pages/backupPages/AppliedStyle';
import AppliedStyleFinal from './pages/AppliedStyleFinal';
import ChooseColor from './pages/backupPages/ChooseColor';
import AppliedColor from './pages/backupPages/AppliedColor';
import History from './pages/History';
import Login from './pages/Login';
import SignUp from './pages/SignUp';


const routes = [
    {
        page : '/Upload',
        component : Upload
    },
    {
        page : '/ChooseStyle',
        component : ChooseStyle
    },
    {
        page : '/AppliedStyle',
        component : AppliedStyle
    },
    {
        page : '/AppliedStyleFinal',
        component : AppliedStyleFinal
    },
    {
        page : '/ChooseColor',
        component : ChooseColor
    },
    {
        page : '/AppliedColor',
        component : AppliedColor
    },
    
    {
        page : '/History',
        component : History
    },
    {
        page : '/',
        component : Login
    },
    {
        page : '/SignUp',
        component : SignUp
    },
    {
        page : '/Title',
        component : Title
    },
    
];

export default routes;