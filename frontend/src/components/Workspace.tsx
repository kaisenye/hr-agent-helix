import React from 'react';

interface WorkspaceProps {
  sequenceText: string;
  setSequenceText: (text: string) => void;
}

const Workspace: React.FC<WorkspaceProps> = ({ sequenceText, setSequenceText }) => {
  return (
    <div style={{ padding: '1rem' }}>
      <h2>Recruiting Outreach Sequence</h2>
      <textarea
        style={{ width: '100%', height: '80vh' }}
        value={sequenceText}
        onChange={(e) => setSequenceText(e.target.value)}
      />
    </div>
  );
};

export default Workspace;
