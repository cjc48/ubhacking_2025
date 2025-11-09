import Chat from '../Components/Chat';
import { useParams } from 'react-router-dom';

export default function ChatPage() {
    // Get the dynamic part of the URL, which we define as 'mentorId' in App.tsx
    const { mentorId } = useParams<{ mentorId: string }>();

    // Render the Chat component, passing the mentorId from the URL as a prop.
    // We provide a fallback to 'socrates' in case the URL is missing the ID.
    return <Chat mentor={mentorId || 'socrates'} />;
}