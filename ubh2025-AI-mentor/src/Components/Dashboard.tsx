import * as React from 'react';
import Chat from './Chat.tsx';
import logo from '../assets/DoppelLogo.png';
import { createTheme } from '@mui/material/styles';
import PsychologyAlt from '@mui/icons-material/PsychologyAlt';
import { AppProvider, type Navigation } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';

/*
*
* TODO
* create a structure that has a mentor's:
* - Profile Photo
* - Name
*
*/

const MentorList : Navigation = [
    {
        segment: 'socrates',
        title: 'Socrates',
        icon: <PsychologyAlt />,
    },
    {
        segment: 'ash',
        title: 'Ash',
        icon: <PsychologyAlt />,
    },
]

const ChatList : Navigation = [
    {
        segment: 'chat1',
        title: 'Chat1',
    },
]

const appTheme = createTheme({
    cssVariables: {
        colorSchemeSelector: 'data-toolpad-color-scheme',
    },
    colorSchemes: { light: true, dark: true },
    breakpoints: {
        values: {
            xs: 0,
            sm: 600,
            md: 600,
            lg: 1200,
            xl: 1536,
        },
    },
});

export default function DashboardLayoutBasic() {
    const [activePage, setActivePage] = React.useState('socrates');

    const router = {
        pathname: activePage,
        navigate: (path: string) => setActivePage(path.split('/').pop() || 'socrates'),
    };


    let nav : Navigation = [{
        kind: 'header',
        title: 'Mentors',
    },];

    nav = nav.concat(MentorList);
    nav = nav.concat([{
            kind: 'divider',
        },
        {
            kind: 'header',
            title: 'Chats',
        },
    ]);
    nav = nav.concat(ChatList);

    return (
        <AppProvider
            navigation={nav}
            router={router}
            theme={appTheme}
            branding={{
                title: '',
                logo: <img src={logo} width={110} alt="Doppel Logo"/>
            }}
        >
            <DashboardLayout>
                <Chat mentor={router.pathname} />
            </DashboardLayout>
        </AppProvider>
    );
}