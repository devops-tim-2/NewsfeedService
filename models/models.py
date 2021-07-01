from dataclasses import dataclass, asdict

from sqlalchemy import Column, Integer, String, Boolean, \
     ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base(name='Model')

@dataclass
class Block(Model):
    __tablename__ = 'block'
    id: int
    src: int
    dst: int

    id = Column(Integer, primary_key=True)
    src = Column(Integer, ForeignKey('userprofile.id'), nullable=False)
    dst = Column(Integer, ForeignKey('userprofile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Block: id={self.id}'


@dataclass
class Follow(Model):
    __tablename__ = 'follow'
    id: int
    mute: bool
    src: int
    dst: int

    id = Column(Integer, primary_key=True)
    mute = Column(Boolean, nullable=False)
    src = Column(Integer, ForeignKey('userprofile.id'), nullable=False)
    dst = Column(Integer, ForeignKey('userprofile.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Follow: id={self.id}'


@dataclass
class Post(Model):
    __tablename__ = 'post'
    id: int

    id = Column(Integer, primary_key=True)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Post: id={self.id}'



@dataclass
class User(Model):
    __tablename__ = 'userprofile'
    id: int
    age: int
    sex: str
    region: str
    interests: str

    id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=False)
    sex = Column(String(127), nullable=False)
    region = Column(String(127), nullable=False)
    interests = Column(String(127), nullable=False)
    
    def __repr__(self):
        return '<User %r>' % self.id

    def get_dict(self):
        return asdict(self)


@dataclass
class Campaign(Model):
    __tablename__ = 'campaign'
    id: int
    age_min: int
    age_max: int
    sex: str
    regions: str
    interests: str

    id = Column(Integer, primary_key=True)
    age_min = Column(Integer, nullable=False)
    age_max = Column(Integer, nullable=False)
    sex = Column(String(127), nullable=False)
    regions = Column(String(127), nullable=False)
    interests = Column(String(127), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'Campaign: id={self.id}'


@dataclass
class CampaignFeed(Model):
    __tablename__ = 'campaignfeed'
    id: int
    u_id: int
    c_id: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    u_id = Column(Integer, ForeignKey('userprofile.id'), nullable=False)
    c_id = Column(Integer, ForeignKey('campaign.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'CampaignFeed: id={self.id}'


@dataclass
class PostFeed(Model):
    __tablename__ = 'postfeed'
    id: int
    u_id: int
    p_id: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    u_id = Column(Integer, ForeignKey('userprofile.id'), nullable=False)
    p_id = Column(Integer, ForeignKey('post.id'), nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'PostFeed: id={self.id}'