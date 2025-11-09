import { createTheme } from '@mui/material/styles';
import PsychologyAlt from '@mui/icons-material/PsychologyAlt';
import AccountCircle from '@mui/icons-material/AccountCircle';
import { AppProvider, type Navigation } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import { useNavigate, useLocation, Outlet } from 'react-router-dom';
import logo from './Assets/DoppelLogo.png'

// 1. Use the full, absolute path for each navigation segment.
const MentorList: Navigation = [
    { segment: '/mentor/socrates', title: 'Socrates', icon: <PsychologyAlt /> },
    { segment: '/mentor/plato', title: 'Plato', icon: <PsychologyAlt /> },
];

const appTheme = createTheme({
    palette: {
        mode: 'dark',
    },
});

export default function Root() {
    const navigate = useNavigate();
    const location = useLocation();

    const router = {
        pathname: location.pathname,
        navigate: (path: string) => navigate(path),
    };

    const navigation: Navigation = [
        { kind: 'header', title: 'Mentors' },
        ...MentorList,
        { kind: 'divider' },
        {
            // This segment MUST be the absolute path to the page.
            segment: '/mydoppel',
            title: 'My Doppel',
            icon: <AccountCircle />,
        },
    ];


    return (
        <AppProvider
            navigation={navigation}
            router={router}
            theme={appTheme}
            branding={{
                title: '',
                logo: <img src={logo} width={100} alt="Doppel Logo" />
            }}
        >
            <DashboardLayout>
                <Outlet />
            </DashboardLayout>
        </AppProvider>
    );
}