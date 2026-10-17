CREATE TABLE participants (
    id BIGINT PRIMARY KEY,
    username TEXT,
    full_name TEXT NOT NULL,
    affiliation_type TEXT NOT NULL,
    bmstu_group TEXT,
    university TEXT,
    passport TEXT,
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE UNIQUE INDEX participants_name_group_uq ON participants (lower(full_name), bmstu_group);
CREATE UNIQUE INDEX participants_passport_uq ON participants (passport);

CREATE TABLE teams (
    id CHAR(8) PRIMARY KEY,
    name TEXT UNIQUE NOT NULL,
    captain_id BIGINT NOT NULL REFERENCES participants(id),
    created_at TIMESTAMPTZ DEFAULT now()
);

CREATE TABLE team_members (
    team_id CHAR(8) REFERENCES teams(id) ON DELETE CASCADE,
    participant_id BIGINT REFERENCES participants(id),
    PRIMARY KEY (team_id, participant_id)
);

CREATE TABLE fsm_states (
    chat_id BIGINT NOT NULL,
    user_id BIGINT NOT NULL,
    state TEXT,
    data JSONB DEFAULT '{}',
    PRIMARY KEY (chat_id, user_id)
);
