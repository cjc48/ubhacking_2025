import Chat from './Chat'
import { createTheme } from '@mui/material/styles';
import PsychologyAlt from '@mui/icons-material/PsychologyAlt';
import { AppProvider, type Navigation } from '@toolpad/core/AppProvider';
import { DashboardLayout } from '@toolpad/core/DashboardLayout';
import { DemoProvider, useDemoRouter } from '@toolpad/core/internal';

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
        segment: 'orders',
        title: 'Orders',
        icon: <PsychologyAlt />,
    },
]

const ChatList : Navigation = [
    {
        segment: 'chat1',
        title: 'Chat1',
    },
]

const demoTheme = createTheme({
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

interface DemoProps {
    /**
     * Injected by the documentation to work in an iframe.
     * Remove this when copying and pasting into your project.
     */
    window?: () => Window;
}

export default function DashboardLayoutBasic(props: DemoProps) {
    const { window } = props;

    const router = useDemoRouter('/dashboard');

    // Remove this const when copying and pasting into your project.
    const demoWindow = window !== undefined ? window() : undefined;

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
        // Remove this provider when copying and pasting into your project.
        <DemoProvider window={demoWindow}>
            {/* preview-start */}
            <AppProvider
                navigation={nav}
                router={router}
                theme={demoTheme}
                window={demoWindow}
            >
                <DashboardLayout>
                    <Chat mentor={router.pathname} />
                </DashboardLayout>
            </AppProvider>
            {/* preview-end */}
        </DemoProvider>
    );
}