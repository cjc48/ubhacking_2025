import * as React from 'react';
import { createTheme } from '@mui/material/styles';
import PsychologyAlt from '@mui/icons-material/PsychologyAlt';
import { AppProvider, type Navigation } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import ProfileMenu from './Components/ProfileMenu';
import { useNavigate, useLocation, Outlet } from 'react-router-dom';
import logo from './Assets/DoppelLogo.png';
import AccountCircle from '@mui/icons-material/AccountCircle';

const MentorList: Navigation = [
    { segment: 'socrates', title: 'Socrates', icon: <PsychologyAlt /> },
    { segment: 'plato', title: 'Plato', icon: <PsychologyAlt /> },
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
        // The AppProvider will call this with a segment like 'socrates'.
        // We now construct the full path: '/mentor/socrates'.
        navigate: (path: string) => {
            const isMentor = MentorList.some(mentor => mentor.segment === path);
            if (isMentor) {navigate(`/mentor${path}`)}
            else {navigate('${path}')}
        },
    };

    const navigation: Navigation = [
        { kind: 'header', title: 'Mentors' },
        ...MentorList,
        { kind: 'divider' }, // A visual separator
        {
            segment: 'mydoppel',
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
                logo: <img src={logo} width={100} alt="AI Mentor Logo" />
            }}
        >
            <DashboardLayout>
                <Outlet />
            </DashboardLayout>
        </AppProvider>
    );
}