import Title from './pages/Title';
import ChooseStyle from './pages/ChooseStyle';
import AppliedStyle from './pages/AppliedStyle';
import AppliedStyleFinal from './pages/AppliedStyleFinal';
import ChooseColor from './pages/ChooseColor';
import AppliedColor from './pages/AppliedColor';
import Final from './pages/Final';
import History from './pages/History';

const routes = [
    {
        page : '/',
        component : Title
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
        page : '/Final',
        component : Final
    },
    {
        page : '/History',
        component : History
    },
];

export default routes;