import maya.cmds as c

windowName = 'rigUI'
if c.window(windowName, exists=True):
    c.deleteUI(windowName)

window = c.window(windowName, title="Biped Rig Generator", iconName='Make Rig', widthHeight=(100, 175) )
c.columnLayout( rowSpacing=10 )
c.text(label="Setup: Make sure your character is facing up the Z-Axis", align='left', wordWrap=True)
c.text(label="Step1: Generate locators and place at joint locations up the spine and on arms/legs on one side of the body", align='left', wordWrap=True)
c.button( label='Generate locators', c='create_locators()')
c.text(label="Step2: After placing the joint locators, generate the rig.", align='left', wordWrap=True)
c.button( label='Generate rig', c='generate_rig()')
c.text(label="Step3: You're ready for skinning! Use this to select all the joints for binding. In your bind skin options, set 'Bind To: selected joints'", align='left', wordWrap=True)

c.button( label='Select joints', c='c.select("jnt_*")')
c.setParent( '..' )
c.showWindow( window )

def create_locators():
    locs = ['shld_pos', 'elbow_pos', 'wrist_pos', 'hip_pos', 'knee_pos', 'ankle_pos', 'toe_pos', 'cog_pos', 'spine_pos', 'chest_pos', 'neck_pos', 'head_pos']
    
    for loc in locs:
        c.spaceLocator(n=loc)

def generate_rig():
    # get position of pos objects
    shld = c.xform('shld_pos', q=True, t=True, ws=True)
    elbow = c.xform('elbow_pos', q=True, t=True, ws=True)
    wrist = c.xform('wrist_pos', q=True, t=True, ws=True)
    hip = c.xform('hip_pos', q=True, t=True, ws=True)
    knee = c.xform('knee_pos', q=True, t=True, ws=True)
    ankle = c.xform('ankle_pos', q=True, t=True, ws=True)
    toe = c.xform('toe_pos', q=True, t=True, ws=True)
    cog = c.xform('cog_pos', q=True, t=True, ws=True)
    spine = c.xform('spine_pos', q=True, t=True, ws=True)
    chest = c.xform('chest_pos', q=True, t=True, ws=True)
    neck = c.xform('neck_pos', q=True, t=True, ws=True)
    head = c.xform('head_pos', q=True, t=True, ws=True)
    
    def midpoint(p1, p2):
        return [(p1[0]+p2[0])/2, (p1[1]+p2[1])/2, (p1[2]+p2[2])/2]
    
    # find position of foot ball
    ball = midpoint(ankle, toe)
    
    # check what side it's on and make mirrored loc
    if shld[0] > 0:
        r_shld = shld
        l_shld = [shld[0]*-1, shld[1], shld [2]]
        r_elbow = elbow
        l_elbow = [elbow[0]*-1, elbow[1], elbow[2]]
        r_wrist = wrist
        l_wrist = [wrist[0]*-1, wrist[1], wrist[2]]
    else:
        l_shld = shld
        r_shld = [shld[0]*-1, shld[1], shld [2]]
        l_elbow = elbow
        r_elbow = [elbow[0]*-1, elbow[1], elbow[2]]
        l_wrist = wrist
        r_wrist = [wrist[0]*-1, wrist[1], wrist[2]]
    
    if hip[0] > 0:
        r_hip = hip
        l_hip = [hip[0]*-1, hip[1], hip [2]]
        r_knee = knee
        l_knee = [knee[0]*-1, knee[1], knee[2]]
        r_ankle = ankle
        l_ankle = [ankle[0]*-1, ankle[1], ankle[2]]
        r_toe = toe
        l_toe = [toe[0]*-1, toe[1], toe[2]]
        r_ball = ball
        l_ball = [ball[0]*-1, ball[1], ball[2]]
    else:
        l_hip = hip
        r_hip = [hip[0]*-1, hip[1], hip [2]]
        l_knee = knee
        r_knee = [knee[0]*-1, knee[1], knee[2]]
        l_ankle = ankle
        r_ankle = [ankle[0]*-1, ankle[1], ankle[2]]
        l_toe = toe
        r_toe = [toe[0]*-1, toe[1], toe[2]]
        l_ball = ball
        r_ball = [ball[0]*-1, ball[1], ball[2]]
    
    # ----------------------------------------
    #                  ARMS
    # ----------------------------------------
        
    # make joints as positions
    # make driver chain
    c.joint(n='jnt_r_shld', p=r_shld)
    c.joint(n='jnt_r_elbow', p=r_elbow)
    c.joint(n='jnt_r_wrist', p=r_wrist)
    c.select('jnt_r_shld')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    c.joint(n='jnt_l_shld', p=l_shld)
    c.joint(n='jnt_l_elbow', p=l_elbow)
    c.joint(n='jnt_l_wrist', p=l_wrist)
    c.select('jnt_l_shld')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    # make fk chain
    c.joint(n='fk_r_shld', p=r_shld)
    c.joint(n='fk_r_elbow', p=r_elbow)
    c.joint(n='fk_r_wrist', p=r_wrist)
    c.select('fk_r_shld')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    c.joint(n='fk_l_shld', p=l_shld)
    c.joint(n='fk_l_elbow', p=l_elbow)
    c.joint(n='fk_l_wrist', p=l_wrist)
    c.select('fk_l_shld')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    # make ik chain
    c.joint(n='ik_r_shld', p=r_shld)
    c.joint(n='ik_r_elbow', p=r_elbow)
    c.joint(n='ik_r_wrist', p=r_wrist)
    c.select('ik_r_shld')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    c.joint(n='ik_l_shld', p=l_shld)
    c.joint(n='ik_l_elbow', p=l_elbow)
    c.joint(n='ik_l_wrist', p=l_wrist)
    c.select('ik_l_shld')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    # ------------------ FK SETUP
    # RIGHT FK
    # create controls and position
    shld_r_cc = c.circle(n='fk_r_shld_cc')
    c.rotate( 0, '90deg', 0, shld_r_cc )
    c.makeIdentity( apply=True )
    c.delete(ch=True)
    c.group('fk_r_shld_cc', n='fk_r_shld_ccg')
    c.parentConstraint('jnt_r_shld', 'fk_r_shld_ccg', mo=False, n='const')
    c.delete('const')
    
    elbow_r_cc = c.circle(n='fk_r_elbow_cc')
    c.rotate( 0, '90deg', 0, elbow_r_cc )
    c.makeIdentity( apply=True )
    c.delete(ch=True)
    c.group('fk_r_elbow_cc', n='fk_r_elbow_ccg')
    c.parentConstraint('jnt_r_elbow', 'fk_r_elbow_ccg', mo=False, n='const')
    c.delete('const')
    
    wrist_r_cc = c.circle(n='fk_r_wrist_cc')
    c.rotate( 0, '90deg', 0, wrist_r_cc )
    c.makeIdentity( apply=True )
    c.delete(ch=True)
    c.group('fk_r_wrist_cc', n='fk_r_wrist_ccg')
    c.parentConstraint('jnt_r_wrist', 'fk_r_wrist_ccg', mo=False, n='const')
    c.delete('const')
    
    c.parent('fk_r_wrist_ccg', 'fk_r_elbow_cc')
    c.parent('fk_r_elbow_ccg', 'fk_r_shld_cc')
    # hide FK controls
    c.select('fk_r_shld_cc')
    c.setAttr('fk_r_shld_cc.visibility', False)
    c.select('fk_r_elbow_cc')
    c.setAttr('fk_r_elbow_cc.visibility', False)
    c.select('fk_r_wrist_cc')
    c.setAttr('fk_r_wrist_cc.visibility', False)
    
    # connect controls to jnts
    c.orientConstraint('fk_r_shld_cc', 'fk_r_shld', mo=False)
    c.orientConstraint('fk_r_elbow_cc', 'fk_r_elbow', mo=False)
    c.orientConstraint('fk_r_wrist_cc', 'fk_r_wrist', mo=False)
    
    # LEFT FK
    # create controls and position
    shld_l_cc = c.circle(n='fk_l_shld_cc')
    c.rotate( 0, '90deg', 0, shld_l_cc )
    c.makeIdentity( apply=True )
    c.delete(ch=True)
    c.group('fk_l_shld_cc', n='fk_l_shld_ccg')
    c.parentConstraint('jnt_l_shld', 'fk_l_shld_ccg', mo=False, n='const')
    c.delete('const')
    
    elbow_l_cc = c.circle(n='fk_l_elbow_cc')
    c.rotate( 0, '90deg', 0, elbow_l_cc )
    c.makeIdentity( apply=True )
    c.delete(ch=True)
    c.group('fk_l_elbow_cc', n='fk_l_elbow_ccg')
    c.parentConstraint('jnt_l_elbow', 'fk_l_elbow_ccg', mo=False, n='const')
    c.delete('const')
    
    wrist_l_cc = c.circle(n='fk_l_wrist_cc')
    c.rotate( 0, '90deg', 0, wrist_l_cc )
    c.makeIdentity( apply=True )
    c.delete(ch=True)
    c.group('fk_l_wrist_cc', n='fk_l_wrist_ccg')
    c.parentConstraint('jnt_l_wrist', 'fk_l_wrist_ccg', mo=False, n='const')
    c.delete('const')
    
    c.parent('fk_l_wrist_ccg', 'fk_l_elbow_cc')
    c.parent('fk_l_elbow_ccg', 'fk_l_shld_cc')
    # hide FK controls
    c.select('fk_l_shld_cc')
    c.setAttr('fk_l_shld_cc.visibility', False)
    c.select('fk_l_elbow_cc')
    c.setAttr('fk_l_elbow_cc.visibility', False)
    c.select('fk_l_wrist_cc')
    c.setAttr('fk_l_wrist_cc.visibility', False)
    
    # connect controls to jnts
    c.orientConstraint('fk_l_shld_cc', 'fk_l_shld', mo=False)
    c.orientConstraint('fk_l_elbow_cc', 'fk_l_elbow', mo=False)
    c.orientConstraint('fk_l_wrist_cc', 'fk_l_wrist', mo=False)
    
    # ------------------ IK SETUP
    # RIGHT IK
    # create IK chain
    c.ikHandle( n='ik_r_arm', sj='ik_r_shld', ee='ik_r_wrist', sol='ikRPsolver')
    # create IK control
    c.circle(n='ik_r_arm_cc')
    c.delete(ch=True)
    # position
    c.parentConstraint('ik_r_wrist', 'ik_r_arm_cc', mo=False, n='const')
    c.delete('const')
    c.rotate( 0, '90deg', 0, 'ik_r_arm_cc' )
    c.scale(0.8, 0.8, 0.8)
    c.makeIdentity( apply=True )
    # connect
    c.pointConstraint('ik_r_arm_cc', 'ik_r_arm')
    c.orientConstraint('ik_r_arm_cc', 'ik_r_wrist')
    c.select('ik_r_arm')
    c.setAttr('ik_r_arm.visibility', False)
    c.setAttr( 'ik_r_arm_cc.visibility', k=False, cb=False)
    
    # LEFT IK
    # create IK chain
    c.ikHandle( n='ik_l_arm', sj='ik_l_shld', ee='ik_l_wrist', sol='ikRPsolver')
    # create IK control
    c.circle(n='ik_l_arm_cc')
    c.delete(ch=True)
    # position
    c.parentConstraint('ik_l_wrist', 'ik_l_arm_cc', mo=False, n='const')
    c.delete('const')
    c.rotate( 0, '90deg', 0, 'ik_l_arm_cc' )
    c.scale(0.8, 0.8, 0.8)
    c.makeIdentity( apply=True )
    # connect
    c.pointConstraint('ik_l_arm_cc', 'ik_l_arm')
    c.orientConstraint('ik_l_arm_cc', 'ik_l_wrist')
    c.select('ik_l_arm')
    c.setAttr('ik_l_arm.visibility', False)
    c.setAttr( 'ik_l_arm_cc.visibility', k=False, cb=False)
    
    
    # ------------------ CONNECT IK/FK CHAINS TO DRIVER CHAIN
    c.orientConstraint( 'fk_r_shld', 'ik_r_shld', 'jnt_r_shld' )
    c.orientConstraint( 'fk_r_elbow', 'ik_r_elbow', 'jnt_r_elbow' )
    c.orientConstraint( 'fk_r_wrist', 'ik_r_wrist', 'jnt_r_wrist' )
    
    c.orientConstraint( 'fk_l_shld', 'ik_l_shld', 'jnt_l_shld' )
    c.orientConstraint( 'fk_l_elbow', 'ik_l_elbow', 'jnt_l_elbow' )
    c.orientConstraint( 'fk_l_wrist', 'ik_l_wrist', 'jnt_l_wrist' )
    
    # set weight of fk chains to 0
    c.orientConstraint( 'fk_r_shld', 'jnt_r_shld', w=0 )
    c.orientConstraint( 'fk_r_elbow', 'jnt_r_elbow', w=0 )
    c.orientConstraint( 'fk_r_wrist', 'jnt_r_wrist', w=0 )
    
    c.orientConstraint( 'fk_l_shld', 'jnt_l_shld', w=0 )
    c.orientConstraint( 'fk_l_elbow', 'jnt_l_elbow', w=0 )
    c.orientConstraint( 'fk_l_wrist', 'jnt_l_wrist', w=0 )
    
    # make control with IKFK attr
    c.circle(n='IKFK_r_cc')
    c.delete(ch=True)
    c.parentConstraint('jnt_r_wrist', 'IKFK_r_cc', n='pos', mo=False)
    c.delete('pos')
    c.makeIdentity( apply=True )
    c.setAttr('IKFK_r_cc.tx', 3)
    c.scale(0.5, 0.5, 0.5)
    c.parent('IKFK_r_cc', 'jnt_r_wrist')
    c.makeIdentity( apply=True)
    c.addAttr( longName='IKFK', at='enum', en="IK:FK", h=False, k=True )
    
    c.circle(n='IKFK_l_cc')
    c.delete(ch=True)
    c.parentConstraint('jnt_l_wrist', 'IKFK_l_cc', n='pos', mo=False)
    c.delete('pos')
    c.makeIdentity( apply=True )
    c.setAttr('IKFK_l_cc.tx', -3)
    c.scale(0.5, 0.5, 0.5)
    c.parent('IKFK_l_cc', 'jnt_l_wrist')
    c.makeIdentity( apply=True)
    c.addAttr( longName='IKFK', at='enum', en="IK:FK", h=False, k=True )
    
    # hide extra attrs
    c.setAttr( 'IKFK_r_cc.translateX', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.translateY', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.translateZ', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.rotateX', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.rotateY', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.rotateZ', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.scaleX', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.scaleY', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.scaleZ', k=False, cb=False)
    c.setAttr( 'IKFK_r_cc.visibility', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.translateX', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.translateY', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.translateZ', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.rotateX', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.rotateY', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.rotateZ', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.scaleX', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.scaleY', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.scaleZ', k=False, cb=False)
    c.setAttr( 'IKFK_l_cc.visibility', k=False, cb=False)
    
    # creating IKFK SDK
    # RIGHT SDK
    # setting keys while in IK mode
    c.select('jnt_r_wrist_orientConstraint1')
    c.setDrivenKeyframe( at='fk_r_wristW0', cd='IKFK_r_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_r_wristW1', cd='IKFK_r_cc.IKFK' )
    c.select('jnt_r_elbow_orientConstraint1')
    c.setDrivenKeyframe( at='fk_r_elbowW0', cd='IKFK_r_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_r_elbowW1', cd='IKFK_r_cc.IKFK' )
    c.select('jnt_r_shld_orientConstraint1')
    c.setDrivenKeyframe( at='fk_r_shldW0', cd='IKFK_r_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_r_shldW1', cd='IKFK_r_cc.IKFK' )
    # hiding fk controls
    c.select('fk_r_shld_cc')
    c.setDrivenKeyframe( at='visibility', cd='IKFK_r_cc.IKFK' )
    c.select('fk_r_elbow_cc')
    c.setDrivenKeyframe( at='visibility', cd='IKFK_r_cc.IKFK' )
    c.select('fk_r_wrist_cc')
    c.setDrivenKeyframe( at='visibility', cd='IKFK_r_cc.IKFK' )
    c.select('ik_r_arm_cc')
    c.setDrivenKeyframe( at='visibility', cd='IKFK_r_cc.IKFK' )
    
    # switch to fk mode
    c.select('IKFK_r_cc')
    c.setAttr('IKFK_r_cc.IKFK', 1)
    
    c.select('jnt_r_wrist_orientConstraint1')
    c.setAttr('jnt_r_wrist_orientConstraint1.fk_r_wristW0', 1)
    c.setAttr('jnt_r_wrist_orientConstraint1.ik_r_wristW1', 0)
    c.setDrivenKeyframe( at='fk_r_wristW0', cd='IKFK_r_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_r_wristW1', cd='IKFK_r_cc.IKFK' )
    
    c.select('jnt_r_elbow_orientConstraint1')
    c.setAttr('jnt_r_elbow_orientConstraint1.fk_r_elbowW0', 1)
    c.setAttr('jnt_r_elbow_orientConstraint1.ik_r_elbowW1', 0)
    c.setDrivenKeyframe( at='fk_r_elbowW0', cd='IKFK_r_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_r_elbowW1', cd='IKFK_r_cc.IKFK' )
    
    c.select('jnt_r_shld_orientConstraint1')
    c.setAttr('jnt_r_shld_orientConstraint1.fk_r_shldW0', 1)
    c.setAttr('jnt_r_shld_orientConstraint1.ik_r_shldW1', 0)
    c.setDrivenKeyframe( at='fk_r_shldW0', cd='IKFK_r_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_r_shldW1', cd='IKFK_r_cc.IKFK' )
    
    c.select('fk_r_shld_cc')
    c.setAttr('fk_r_shld_cc.visibility', True)
    c.setDrivenKeyframe( at='visibility', cd='IKFK_r_cc.IKFK' )
    c.select('fk_r_elbow_cc')
    c.setAttr('fk_r_elbow_cc.visibility', True)
    c.setDrivenKeyframe( at='visibility', cd='IKFK_r_cc.IKFK' )
    c.select('fk_r_wrist_cc')
    c.setAttr('fk_r_wrist_cc.visibility', True)
    c.setDrivenKeyframe( at='visibility', cd='IKFK_r_cc.IKFK' )
    c.select('ik_r_arm_cc')
    c.setAttr('ik_r_arm_cc.visibility', False)
    c.setDrivenKeyframe( at='visibility', cd='IKFK_r_cc.IKFK' )
    
    c.select('IKFK_r_cc')
    c.setAttr('IKFK_r_cc.IKFK', 0)
    # LEFT SDK
    c.select('jnt_l_wrist_orientConstraint1')
    c.setDrivenKeyframe( at='fk_l_wristW0', cd='IKFK_l_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_l_wristW1', cd='IKFK_l_cc.IKFK' )
    c.select('jnt_l_elbow_orientConstraint1')
    c.setDrivenKeyframe( at='fk_l_elbowW0', cd='IKFK_l_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_l_elbowW1', cd='IKFK_l_cc.IKFK' )
    c.select('jnt_l_shld_orientConstraint1')
    c.setDrivenKeyframe( at='fk_l_shldW0', cd='IKFK_l_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_l_shldW1', cd='IKFK_l_cc.IKFK' )
    
    c.select('fk_l_shld_cc')
    c.setDrivenKeyframe( at='visibility', cd='IKFK_l_cc.IKFK' )
    c.select('fk_l_elbow_cc')
    c.setDrivenKeyframe( at='visibility', cd='IKFK_l_cc.IKFK' )
    c.select('fk_l_wrist_cc')
    c.setDrivenKeyframe( at='visibility', cd='IKFK_l_cc.IKFK' )
    c.select('ik_l_arm_cc')
    c.setDrivenKeyframe( at='visibility', cd='IKFK_l_cc.IKFK' )
    
    c.select('IKFK_l_cc')
    c.setAttr('IKFK_l_cc.IKFK', 1)
    
    c.select('jnt_l_wrist_orientConstraint1')
    c.setAttr('jnt_l_wrist_orientConstraint1.fk_l_wristW0', 1)
    c.setAttr('jnt_l_wrist_orientConstraint1.ik_l_wristW1', 0)
    c.setDrivenKeyframe( at='fk_l_wristW0', cd='IKFK_l_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_l_wristW1', cd='IKFK_l_cc.IKFK' )
    
    c.select('jnt_l_elbow_orientConstraint1')
    c.setAttr('jnt_l_elbow_orientConstraint1.fk_l_elbowW0', 1)
    c.setAttr('jnt_l_elbow_orientConstraint1.ik_l_elbowW1', 0)
    c.setDrivenKeyframe( at='fk_l_elbowW0', cd='IKFK_l_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_l_elbowW1', cd='IKFK_l_cc.IKFK' )
    
    c.select('jnt_l_shld_orientConstraint1')
    c.setAttr('jnt_l_shld_orientConstraint1.fk_l_shldW0', 1)
    c.setAttr('jnt_l_shld_orientConstraint1.ik_l_shldW1', 0)
    c.setDrivenKeyframe( at='fk_l_shldW0', cd='IKFK_l_cc.IKFK' )
    c.setDrivenKeyframe( at='ik_l_shldW1', cd='IKFK_l_cc.IKFK' )
    
    c.select('fk_l_shld_cc')
    c.setAttr('fk_l_shld_cc.visibility', True)
    c.setDrivenKeyframe( at='visibility', cd='IKFK_l_cc.IKFK' )
    c.select('fk_l_elbow_cc')
    c.setAttr('fk_l_elbow_cc.visibility', True)
    c.setDrivenKeyframe( at='visibility', cd='IKFK_l_cc.IKFK' )
    c.select('fk_l_wrist_cc')
    c.setAttr('fk_l_wrist_cc.visibility', True)
    c.setDrivenKeyframe( at='visibility', cd='IKFK_l_cc.IKFK' )
    c.select('ik_l_arm_cc')
    c.setAttr('ik_l_arm_cc.visibility', False)
    c.setDrivenKeyframe( at='visibility', cd='IKFK_l_cc.IKFK' )
    
    c.select('IKFK_l_cc')
    c.setAttr('IKFK_l_cc.IKFK', 0)
    
    
    # ----------------------------------------
    #                  LEGS
    # ----------------------------------------
    
    # make joints at positions
    c.select(clear=True)
    c.joint(n='jnt_r_hip', p=r_hip)
    c.joint(n='jnt_r_knee', p=r_knee)
    c.joint(n='jnt_r_ankle', p=r_ankle)
    c.joint(n='jnt_r_ball', p=r_ball)
    c.joint(n='jnt_r_toe', p=r_toe)
    c.select('jnt_r_hip')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    c.joint(n='jnt_l_hip', p=l_hip)
    c.joint(n='jnt_l_knee', p=l_knee)
    c.joint(n='jnt_l_ankle', p=l_ankle)
    c.joint(n='jnt_l_ball', p=l_ball)
    c.joint(n='jnt_l_toe', p=l_toe)
    c.select('jnt_l_hip')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    c.joint(n='jnt_hula', p=[cog[0], (cog[1] - 0.05), cog[2]])
    c.select(clear=True)
    c.parent('jnt_l_hip', 'jnt_r_hip', 'jnt_hula')
    c.select(clear=True)
    
    # ------------------ IK SETUP
    # RIGHT IK
    # create IK chain
    c.ikHandle( n='ik_r_leg', sj='jnt_r_hip', ee='jnt_r_ankle', sol='ikRPsolver')
    # create IK control
    c.circle(n='ik_r_leg_cc')
    c.delete(ch=True)
    # position
    c.parentConstraint('jnt_r_ankle', 'ik_r_leg_cc', mo=False, n='const')
    c.delete('const')
    c.rotate( '90deg', 0, 0, 'ik_r_leg_cc' )
    c.scale(0.8, 0.8, 0.8)
    c.makeIdentity( apply=True )
    # connect
    c.pointConstraint('ik_r_leg_cc', 'ik_r_leg')
    c.orientConstraint('ik_r_leg_cc', 'jnt_r_ankle', mo=True)
    c.select('ik_r_leg')
    c.setAttr('ik_r_leg.visibility', False)
    c.setAttr( 'ik_r_leg_cc.visibility', k=False, cb=False)
    
    # LEFT IK
    # create IK chain
    c.ikHandle( n='ik_l_leg', sj='jnt_l_hip', ee='jnt_l_ankle', sol='ikRPsolver')
    # create IK control
    c.circle(n='ik_l_leg_cc')
    c.delete(ch=True)
    # position
    c.parentConstraint('jnt_l_ankle', 'ik_l_leg_cc', mo=False, n='const')
    c.delete('const')
    c.rotate( '90deg', 0, 0, 'ik_l_leg_cc' )
    c.scale(0.8, 0.8, 0.8)
    c.makeIdentity( apply=True )
    # connect
    c.pointConstraint('ik_l_leg_cc', 'ik_l_leg')
    c.orientConstraint('ik_l_leg_cc', 'jnt_l_ankle', mo=True)
    c.select('ik_l_leg')
    c.setAttr('ik_l_leg.visibility', False)
    c.setAttr( 'ik_l_leg_cc.visibility', k=False, cb=False)
    
    # ----------------------------------------
    #                  SPINE
    # ----------------------------------------
    
    c.select(clear=True)
    
    # make joints
    c.joint(n='jnt_cog', p=cog)
    c.joint(n='jnt_spine', p=spine)
    c.joint(n='jnt_chest', p=chest)
    c.joint(n='jnt_neck', p=neck)
    c.joint(n='jnt_head', p=head)
    c.select('jnt_cog')
    c.joint(edit=True, oj='xyz', sao='yup', ch=True, zso=True)
    c.select(clear=True)
    
    c.circle(n='cc_cog')
    c.delete(ch=True)
    c.parentConstraint('jnt_cog', 'cc_cog', mo=False, n='const')
    c.delete('const')
    c.rotate('90deg', 0, 0, 'cc_cog')
    c.scale(3, 3, 3)
    c.makeIdentity( apply=True )
    c.select(clear=True)
    
    c.circle(n='cc_hula')
    c.delete(ch=True)
    c.parentConstraint('jnt_hula', 'cc_hula', mo=False, n='const')
    c.delete('const')
    c.rotate(0, 0, 0, 'cc_hula')
    c.scale(2.5, 1, 1)
    c.makeIdentity( apply=True )
    c.select(clear=True)
    
    c.circle(n='cc_spine')
    c.delete(ch=True)
    c.parentConstraint('jnt_spine', 'cc_spine', mo=False, n='const')
    c.delete('const')
    c.rotate('90deg', 0, 0, 'cc_spine')
    c.scale(2, 2, 2)
    c.makeIdentity( apply=True )
    c.select(clear=True)
    
    c.circle(n='cc_chest')
    c.delete(ch=True)
    c.parentConstraint('jnt_chest', 'cc_chest', mo=False, n='const')
    c.delete('const')
    c.rotate('90deg', 0, 0, 'cc_chest')
    c.scale(2, 2, 2)
    c.makeIdentity( apply=True )
    c.select(clear=True)
    
    c.circle(n='cc_neck')
    c.delete(ch=True)
    c.parentConstraint('jnt_neck', 'cc_neck', mo=False, n='const')
    c.delete('const')
    c.rotate('90deg', 0, 0, 'cc_neck')
    c.scale(1.5, 1.5, 1.5)
    c.makeIdentity( apply=True )
    c.select(clear=True)
    
    c.circle(n='cc_head')
    c.delete(ch=True)
    c.xform('cc_head', piv=[0, -1, 0], ws=True )
    c.parentConstraint('jnt_head', 'cc_head', mo=False, n='const')
    c.delete('const')
    c.scale(2, 2, 2)
    c.makeIdentity( apply=True )
    
    c.parentConstraint('cc_cog', 'jnt_cog', mo=True)
    c.orientConstraint('cc_spine', 'jnt_spine', mo=True)
    c.orientConstraint('cc_chest', 'jnt_chest', mo=True)
    c.orientConstraint('cc_neck', 'jnt_neck', mo=True)
    c.orientConstraint('cc_head', 'jnt_head', mo=True)
    c.orientConstraint('cc_hula', 'jnt_hula', mo=True)
    
    c.parent('cc_hula', 'cc_cog')
    c.parent('cc_head', 'cc_neck')
    c.parent('cc_neck', 'cc_chest')
    c.parent('cc_chest', 'cc_spine')
    c.parent('cc_spine', 'cc_cog')
    c.parent('jnt_r_shld', 'ik_r_shld', 'fk_r_shld', 'jnt_chest')
    c.parent('jnt_l_shld', 'ik_l_shld', 'fk_l_shld', 'jnt_chest')
    c.parent('jnt_hula', 'jnt_cog')
    c.parent('fk_r_shld_ccg', 'fk_l_shld_ccg', 'cc_chest')
    
    c.group('jnt_cog', n='jnts')
    c.group(['cc_cog', 'ik_r_arm_cc', 'ik_l_arm_cc', 'ik_r_leg_cc', 'ik_l_leg_cc'], n='ccs')
    c.group(['ik_r_arm', 'ik_l_arm', 'ik_r_leg', 'ik_l_leg'], n='iks')
    c.group(['jnts','ccs', 'iks'], n='rig')
    
    c.select(clear=True)
    c.circle(n='masterControl')
    c.rotate('90deg', 0, 0, 'masterControl')
    c.scale(5, 5, 5)
    c.makeIdentity(apply=True)
    c.delete(ch=True)
    
    c.parent('rig', 'masterControl')
    c.select(clear=True)
    
    c.select('*_pos')
    c.delete()
